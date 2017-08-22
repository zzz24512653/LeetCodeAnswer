class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path is None:
            return None
        items = path.split('/')
        ret = []
        for item in items:
            if item == '' or item == '.':
                continue
            elif item == '..':
                if len(ret) != 0:
                    ret.pop()
            else:
                ret.append(item)
        return '/' + '/'.join(ret)
