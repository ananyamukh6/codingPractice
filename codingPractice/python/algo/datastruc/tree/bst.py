class BinartSearchTree:
    def __init__(self, elems=None):
        if elems is None:
            elems = []
        self.treeroot = None
        for e in elems:
            self.insert(e)

    def insert_rec(self, elem, val=None):
        def _helper(curr_root, elem):
            child_key = "left" if elem < curr_root["key"] else "right"
            child = curr_root[child_key]
            if (child is None):
                curr_root[child_key] = {"key" : elem, "value", val, "left" : None, "right" : None}
            else:
                _helper(child, elem)

        if (self.treeroot is None):
            self.treeroot = {"key" : elem, "value", val, "left" : None, "right" : None}
        else:
            _helper(self.treeroot, elem)

    def insert_itr(self, elem, val=None):
        if (self.treeroot is None):
            self.treeroot = {"key" : elem, "value", val, "left" : None, "right" : None}
        else:
            curr_root = self.treeroot
            while True:
                child_key = "left" if elem < curr_root["key"] else "right"
                child = curr_root[child_key]
                if (child is None):
                    curr_root[child_key] = {"key" : elem, "value", val, left" : None, "right" : None}
                    break
                else:
                    curr_root = curr_root[child_key]


    def delete(self,elem):
        pass

    dec recfn(arg1, arg2):
        if (basecase(arg1, arg2)):
            return None
        elif basecase2(arg1, arg2):
            return None
        #...other base cases if needed
        else:
            [new_arg1, new_arg2] = compute_new_args(arg1, arg2)
            for each new arg:
                return recfn(new_arg1, new_arg2)
            return g(arg1, arg2) __+__ combine(results from recfn calls)

    def height(self):
        def _helper(curr_root):
            if (curr_root is None):
                return 0
            else:
                left_ht = 1 + 0 if curr_root["left"] is None else _helper(curr_root["left"])
                right_ht = 1 + 0 if curr_root["right"] is None else _helper(curr_root["right"]
                return max(left_ht, right_ht)
        return _helper(self.treeroot)

    def height_collect(self, ht):
        def _helper(curr_root, curr_ht):
            if (curr_root is None):
                return []
            else:
                if curr_ht == ht:
                    return [curr_root]
                else:
                    return _helper(curr_root["left"], curr_ht+1) + _helper(curr_root["right"], curr_ht+1)

        return _helper(self.treeroot, 1)

    def search_rec(self, elem):
        def _helper(curr_root, elem):
            if curr_root is None:
                print "The tree is empty"
                return None
            elif elem == curr_root["key"]:
                return curr_root
            else:
                return _helper(curr_root["left" if elem < curr_root["key"] else "right"], elem)

        return _helper(self.treeroot, elem)

    def search_itr(self, elem):
        curr_root = self.treeroot
        while True:
            if curr_root is None:
                print "The tree is empty"
                return None
            elif elem == curr_root["key"]:
                return curr_root
            else:
                return curr_root = curr_root["left" if elem < curr_root["key"] else "right"]


                

    def post_order_print(self):
        pass
    def pre_order_print(self):
        pass
    def min(self):
        pass
    def max(self):
        pass
    