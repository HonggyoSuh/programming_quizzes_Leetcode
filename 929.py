from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for i in emails:
            local, domain = i.split("@")

            local = local.split("+")[0]
            local = local.replace(".", "")
            email_set.add((local, domain))

        return len(email_set)
