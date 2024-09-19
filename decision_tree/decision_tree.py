import numpy as np

class Node:
    def __init__(self, left=None, right=None, threshold=None, feature_index=None, info_gain=None, value=None):
        """
        初始化节点:
        - left: 左子节点
        - right: 右子节点
        - threshold: 分裂阈值
        - feature_index: 选择的特征下标
        - info_gain: 信息增益
        - value: 如果是叶子节点，存储预测值
        """
        self.left = left
        self.right = right
        self.threshold = threshold
        self.feature_index = feature_index
        self.info_gain = info_gain
        self.value = value


def entropy(y):
    """
    计算熵（Entropy）
    - y: 标签
    """
    unique, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return -np.sum(probabilities * np.log2(probabilities))


def cal_info_gain(y, y_left, y_right):
    """
    计算信息增益
    - y: 原始标签
    - y_left, y_right: 分裂后的左右子集标签
    """
    parent_entropy = entropy(y)
    left_entropy = entropy(y_left)
    right_entropy = entropy(y_right)
    weight_left = len(y_left) / len(y)
    weight_right = len(y_right) / len(y)
    return parent_entropy - (weight_left * left_entropy + weight_right * right_entropy)


# Let's fix the issue by ensuring that info_gain is never None and info_gain_threshold has a proper default.

class DecisionTreeFixed:
    def __init__(self, max_depth=None, info_gain_threshold=0.01):  # Set a default threshold
        self.max_depth = max_depth
        self.info_gain_threshold = info_gain_threshold
        self.root = None

    def _best_split(self, X, y):
        best_feature = None
        best_threshold = None
        best_info_gain = -1
        n_samples, n_features = X.shape

        for feature_index in range(n_features):
            thresholds = np.unique(X[:, feature_index])  # 获取当前特征的唯一值
            for threshold in thresholds:
                left_indices = X[:, feature_index] < threshold
                right_indices = ~left_indices

                if np.sum(left_indices) == 0 or np.sum(right_indices) == 0:
                    continue

                y_left, y_right = y[left_indices], y[right_indices]
                info_gain = cal_info_gain(y, y_left, y_right)

                if info_gain > best_info_gain:
                    best_feature = feature_index
                    best_threshold = threshold
                    best_info_gain = info_gain

        # Ensure info_gain is never None
        if best_info_gain == -1:
            return None, None, 0  # Return 0 as default info_gain

        return best_feature, best_threshold, best_info_gain

    def _build_tree(self, X, y, depth):
        unique_labels = np.unique(y)
        if len(unique_labels) == 1:
            return Node(value=unique_labels[0])

        if depth >= self.max_depth:
            return Node(value=unique_labels[np.argmax(np.bincount(y))])

        feature_index, threshold, info_gain = self._best_split(X, y)
        if info_gain is None or info_gain < self.info_gain_threshold:
            return Node(value=unique_labels[np.argmax(np.bincount(y))])

        left_indices = X[:, feature_index] < threshold
        right_indices = ~left_indices

        X_left, y_left = X[left_indices], y[left_indices]
        X_right, y_right = X[right_indices], y[right_indices]

        left_child = self._build_tree(X_left, y_left, depth + 1)
        right_child = self._build_tree(X_right, y_right, depth + 1)

        return Node(left=left_child, right=right_child, threshold=threshold, feature_index=feature_index, info_gain=info_gain)

    def fit(self, X, y):
        self.root = self._build_tree(X, y, depth=0)

    def predict(self, X):
        def _predict_sample(node, x):
            if node.value is not None:
                return node.value
            if x[node.feature_index] < node.threshold:
                return _predict_sample(node.left, x)
            else:
                return _predict_sample(node.right, x)
        return np.array([_predict_sample(self.root, x) for x in X])



