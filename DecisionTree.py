import math
from collections import Counter

# Dataset from your notebook - 14 rows
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

features = ['Outlook', 'Temp', 'Humidity', 'Wind']
target_idx = -1

def entropy(rows):
    """E(S) = -Σ p_i * log2(p_i)"""
    labels = [row[target_idx] for row in rows]
    total = len(rows)
    counts = Counter(labels)
    
    ent = 0
    print(f" Class counts: {dict(counts)}")
    for label, count in counts.items():
        p = count / total
        ent -= p * math.log2(p)
        print(f" p({label}) = {count}/{total} = {p:.3f}, -p*log2(p) = {-p * math.log2(p):.3f}")
    print(f" Entropy = {ent:.3f}")
    return ent

def split_data(rows, col_idx, value):
    return [row for row in rows if row[col_idx] == value]

def info_gain(rows, col_idx, feature_name):
    """Gain(S,A) = E(S) - Σ |Sv|/|S| * E(Sv)"""
    print(f"\n{'='*60}")
    print(f"CALCULATING INFO GAIN FOR: {feature_name}")
    print(f"{'='*60}")
    
    total_entropy = entropy(rows)
    print(f" Total E(S) = {total_entropy:.3f}")
    
    values = set(row[col_idx] for row in rows)
    weighted_entropy = 0
    
    for val in values:
        subset = split_data(rows, col_idx, val)
        print(f"\n -> Subset {feature_name} = {val}: {len(subset)} samples")
        e = entropy(subset)
        weight = len(subset) / len(rows)
        weighted_part = weight * e
        weighted_entropy += weighted_part
        print(f" Weighted: {len(subset)}/{len(rows)} * {e:.3f} = {weighted_part:.3f}")
    
    gain = total_entropy - weighted_entropy
    print(f"\n Gain({feature_name}) = {total_entropy:.3f} - {weighted_entropy:.3f} = {gain:.3f}")
    print(f"{'='*60}")
    return gain

def build_id3_tree(rows, features_idx, feature_names, depth=0):
    indent = " " * depth
    labels = [row[target_idx] for row in rows]
    
    print(f"\n{indent}{'#'*50}")
    print(f"{indent}LEVEL {depth} | Samples: {len(rows)}")
    print(f"{indent}Distribution: {dict(Counter(labels))}")
    print(f"{indent}{'#'*50}")
    
    # Base case 1: All same class
    if len(set(labels)) == 1:
        print(f"{indent}LEAF NODE: Pure class = {labels[0]}")
        return labels
    
    # Base case 2: No features left
    if not features_idx:
        majority = Counter(labels).most_common(1)[0]
        print(f"{indent}LEAF NODE: Majority vote = {majority}")
        return majority
    
    # Calculate info gain for all remaining features
    gains = []
    for i in features_idx:
        g = info_gain(rows, i, feature_names[i])
        gains.append((g, i))
    
    # Pick best feature with max gain
    best_gain, best_col_idx = max(gains, key=lambda x: x)
    best_feature = feature_names[best_col_idx]
    
    print(f"\n{indent}>>> BEST FEATURE: {best_feature} with Gain = {best_gain:.3f} <<<")
    
    tree = {best_feature: {}}
    remaining_features = [f for f in features_idx if f!= best_col_idx]
    
    # Split on best feature
    for val in sorted(set(row[best_col_idx] for row in rows)):
        print(f"\n{indent}-- Branch: {best_feature} = {val} --")
        subset = split_data(rows, best_col_idx, val)
        subtree = build_id3_tree(subset, remaining_features, feature_names, depth + 1)
        tree[best_feature][val] = subtree
    
    return tree

def print_tree(tree, depth=0):
    """Pretty print the final tree"""
    if not isinstance(tree, dict):
        return str(tree)
    
    result = []
    for feature, branches in tree.items():
        result.append(feature)
        for val, subtree in branches.items():
            result.append(" " * (depth + 1) + f"|-- {val}: {print_tree(subtree, depth + 1)}")
    return "\n".join(result)

def predict(tree, sample, feature_names):
    """Predict using built tree"""
    if not isinstance(tree, dict):
        return tree
    
    feature = list(tree.keys())
    value = sample[feature_names.index(feature)]
    subtree = tree[feature][value]
    return predict(subtree, sample, feature_names)

# ==================== RUN ====================
print("DECISION TREE USING ID3 - PLAYTENNIS DATASET")
print("Formula: Gain(S,A) = Entropy(S) - Σ |Sv|/|S| * Entropy(Sv)")

final_tree = build_id3_tree(data, list(range(4)), features)

print(f"\n\n{'*'*60}")
print("FINAL DECISION TREE:")
print(f"{'*'*60}")
print(print_tree(final_tree))

# Test prediction
print(f"\n{'*'*60}")
print("TESTING:")
test1 = ['Sunny', 'Cool', 'High', 'Strong'] # Should be No
test2 = ['Rain', 'Mild', 'Normal', 'Weak'] # Should be Yes
print(f"['Sunny', 'Cool', 'High', 'Strong'] -> {predict(final_tree, test1, features)}")
print(f"['Rain', 'Mild', 'Normal', 'Weak'] -> {predict(final_tree, test2, features)}")
