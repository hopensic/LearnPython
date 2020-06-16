from collections import defaultdict, deque
from random import randint
from typing import List
from bisect import bisect_left, bisect, insort
from itertools import accumulate
import operator

from leecode.common.common_class import TreeNode
from leecode.common.official import stringToTreeNode
import re


class Solution:

    def validIPAddress(self, IP: str) -> str:
        IPV4, IPV6, NEITHER = "IPv4", "IPv6", "Neither"
        ipv4_pattern = '^((([0-9]|([1-9][0-9])|(1[0-9]{2})|(2[0-4][0-9])|(25[0-5]))(\.)){4})$'
        ipv6_pattern = '^(((([0-9]|[a-f]|[A-F]){1,4})(\:)){8})$'
        if re.compile(ipv4_pattern).match(IP + "."):
            return IPV4
        elif re.compile(ipv6_pattern).match(IP + ":"):
            return IPV6
        else:
            return NEITHER


string = "123.10.2.1"
# string = "2001:0db8:85a3:0:0:8A2E:0370:7334"
s1 = Solution()
t = s1.validIPAddress(string)
print(t)
