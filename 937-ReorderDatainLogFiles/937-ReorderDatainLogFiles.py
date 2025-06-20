# Last updated: 5/31/2025, 12:06:23 AM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # i need to know which is a letter log and which is a dig log
        # for that i need to skip the first word then check through the rest of the string , maybe checking the ord if betwen 0 and 9 or not
        # once i know i sort the letter logs befor the dig logs
        # dig words keep their ordering in the intial array
        # letter words are sorted with alphabetical of the post-identifers string if the same then by identifier
        # u will need to use sort with lambda
        # logsArr[i] = logs[i].split(" ")-> array of each log words
        # logsArr[i][1:] - > all words of a log except the identifier
        # logsArr[i][0] -> identifier
        # res = [] -> list of priorties in sorting
        # for i in range(len(logs)):
        #   logsArr = logs[i].split()
        #   for c in logsArr[1:]:
        #       if ord('0') > ord(c) or ord(c) > ord('9'):
        #           res.append([logs[i], 0]) # 0 means its letteral
        #    res.append([logs[i], 1]) # 1 means its digitis
        # letter_logs = [log for log, p in res if p == 0]
        # letter_logs.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        # digit_logs = [log for log, p in res if p == 1]
        # final_logs = letter_logs + digit_logs

        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda log: (log.split()[1:], log.split()[0]))

        return letter_logs + digit_logs