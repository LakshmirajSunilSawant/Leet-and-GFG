class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        # Map ruleKey to index
        key_map = {"type": 0, "color": 1, "name": 2}
        index = key_map[ruleKey]
        
        count = 0
        
        for item in items:
            if item[index] == ruleValue:
                count += 1
        
        return count