class Solution:
    def numUniqueEmails(self, emails) -> int:
        t = set()
        for email in emails:
            t.add(self.handle_email(email))
        return len(t)

    def handle_email(self, email):
        if email.count('+') > 0:
            return email[:email.index('+')].replace('.', '') + email[email.index('@'):]
        else:
            return email[:email.index('@')].replace('.', '') + email[email.index('@'):]


lst =["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",\
      "testemail+david@lee.tcode.com"]

s = Solution()
print(s.numUniqueEmails(lst))
