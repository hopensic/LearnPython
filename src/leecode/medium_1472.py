from datetime import datetime
from typing import List

'''
tag: ^1472 ^medium ^design
name: ^(Design Browser History)
'''


class BrowserHistory:

    def __init__(self, homepage: str):
        self.maxvalue = 0
        self.homepage = homepage
        self.cur_pos = 0
        self.lst = [homepage]

    def visit(self, url: str) -> None:
        if self.cur_pos == self.maxvalue:
            if self.maxvalue==len(self.lst)-1:
                self.lst.append(url)
            else:
                self.lst[self.maxvalue+1]=url
            self.maxvalue += 1
            self.cur_pos += 1
        else:
            self.cur_pos += 1
            self.maxvalue = self.cur_pos
            self.lst[self.cur_pos] = url

    def back(self, steps: int) -> str:
        if steps > self.cur_pos:
            self.cur_pos = 0
        else:
            self.cur_pos -= steps
        return self.lst[self.cur_pos]

    def forward(self, steps: int) -> str:
        if steps > self.maxvalue - self.cur_pos:
            self.cur_pos = self.maxvalue
        else:
            self.cur_pos += steps
        return self.lst[self.cur_pos]


b = BrowserHistory("esgriv")
b.visit("cgrt")
b.visit("tip")
b.back(9)
b.visit("ktt")
b.forward(7)
b.visit("crgie")
b.visit("iybch")
b.forward(5)
print(1)