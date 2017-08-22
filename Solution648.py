class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if dict is None or len(dict) == 0:
            return sentence

        roots = sorted(dict, key=lambda x: len(x))
        print(roots)
        words = sentence.split(' ')
        ret = []
        for w in words:
            tag = True
            for root in roots:
                if w.startswith(root):
                    ret.append(root)
                    tag = False
                    break
            if tag:
                ret.append(w)
        return ' '.join(ret)
