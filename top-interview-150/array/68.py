def divide(space_left, divide_bw):
    ret = [space_left // divide_bw for _ in range(divide_bw)]
    space_left = space_left % divide_bw
    for i in range(space_left):
        ret[i] += 1
    return ret


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        just = []
        width = 0
        temp = []
        it = iter(words)
        next_word = None
        while True:
            try:
                word = next_word or next(it)
                # print(next_word, word)
                next_word = None
                temp.append(word)
                width += len(word)

                if width == maxWidth:
                    width = 0
                    just.append(temp)
                    temp = []
                elif width > maxWidth:
                    next_word = word
                    width = 0
                    temp.pop()
                    just.append(temp)
                    temp = []
                elif width < maxWidth:
                    width += 1
            except StopIteration:
                break
        if temp != []:
            just.append(temp)
        # print(just)

        ret = []
        for i in range(len(just) - 1):
            line = just[i]
            space_left = maxWidth - len(" ".join(line))
            divide_bw = len(line) - 1
            # print(space_left, divide_bw)
            if divide_bw == 0:
                ret.append(" ".join(line) + " " * space_left)
            else:
                div = divide(space_left, divide_bw)
                # print(div)
                temp_str = ""
                for j, word in enumerate(line):
                    try:
                        temp_str += word + " " * (div[j] + 1)
                    except IndexError:
                        temp_str += word

                ret.append(temp_str)
        last_line = " ".join(just[-1])
        ret.append(last_line + " " * (maxWidth - len(last_line)))
        print(ret)
        return ret


s = Solution()
s.fullJustify(
    words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16
)
s.fullJustify(
    words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
)
s.fullJustify(
    words=[
        "Science",
        "is",
        "what",
        "we",
        "understand",
        "well",
        "enough",
        "to",
        "explain",
        "to",
        "a",
        "computer.",
        "Art",
        "is",
        "everything",
        "else",
        "we",
        "do",
        "it",
    ],
    maxWidth=20,
)
