from collections import defaultdict

def groupAnagrams(strs):
        result = defaultdict(list) ## mapping charcount to list of Anagram
        for s in strs:
            count = [0] * 26 ## a to z

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()

if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))