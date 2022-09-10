import string


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = [None for _ in range(58)]


class SST:
    def __init__(self, li=None):
        self.ascii_list = {key: i for i, key in enumerate(string.ascii_letters + string.whitespace)}
        self.root = None
        if li:
            for i, j in li:
                self.put(i, j)

    def get(self, key: str):
        node = self._get(self.root, key, 0)
        if node: return node.val
        return None

    def _get(self, node, key: str, d):
        if not node: return None
        if d == len(key): return node
        ch_id = self.ascii_list[key[d]]
        return self._get(node.next[ch_id], key, d + 1)

    def put(self, key: str, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, node, key: str, val, d):
        if not node: node = Node()
        if d == len(key):
            node.val = val
            return node
        ch_id = self.ascii_list[key[d]]
        node.next[ch_id] = self._put(node.next[ch_id], key, val, d + 1)
        return node

    def delete(self, key: str):
        self.root = self._delete(self.root, key, 0)

    def _delete(self, node: Node, key, idx):
        if not node: return None
        if idx == len(key):
            node.val = None
        else:
            ch_id = self.ascii_list[key[idx]]
            node.next[ch_id] = self._delete(node.next[ch_id], key, idx + 1)
        if node.val: return node

        for i in range(len(self.ascii_list)):
            if node.next[i]: return node
        return None


if __name__ == '__main__':
    li = [('aac', 2), ('bba', 11), ('csd', 25), ('avc', 6), ('cds', 8)]
    sst = SST(li)
    sst.delete('avc')
    print(sst.get('avc'))
