class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            parts = email.split('@')
            parts[0] = parts[0].replace('.','')

            for i in range(len(parts[0])):
                if parts[0][i] == '+':
                    parts[0] = parts[0][:i]
                    break
            email_set.add('@'.join(parts))

        return len(email_set)

Solution().numUniqueEmails(
["test.email+alex@leetcode.com", "test.email@leetcode.com"])
