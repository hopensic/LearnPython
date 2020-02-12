'''
tag: ^0535 ^hashtable ^math
name: ^(Encode and Decode TinyURL)
'''


class Codec:
    prefix = 'http://tinyurl.com/'

    def __init__(self):
        self.chars = []
        self.chars.extend([i for i in range(48, 58)])
        self.chars.extend([i for i in range(97, 123)])
        self.chars.extend([i for i in range(65, 91)])
        self.char_arr = [chr(ch) for ch in self.chars]
        self.dic = {self.char_arr[k]: k for k in range(62)}
        self.num = 1
        self.url2str_dic = {}
        self.str2url_dic = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tmp = self.url2str_dic.get(longUrl, None)
        if tmp:
            return Codec.prefix + tmp
        else:
            tmp = ''.join([self.char_arr[n] for n in self.convert_to_62decimal(self.num)])
            self.url2str_dic[longUrl] = tmp
            self.str2url_dic[tmp] = longUrl
            res = Codec.prefix + tmp
            self.num += 1
            return res

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        arr = shortUrl[19:]
        return self.str2url_dic[''.join(arr)]

    def convert_to_62decimal(self, num):
        res = []
        while num > 0:
            res.append(num % 62)
            num = int(num / 62)
        return res


# Your Codec object will be instantiated and called as such:

url = 'http://www.baidu.com'
url2 = 'http://www.baidu.com2'
codec = Codec()
# print(codec.encode(url))
# print(codec.encode(url2))
coded = codec.encode(url)
print(coded)
decoded = codec.decode(coded)
print(decoded)


coded = codec.encode(url2)
print(coded)
decoded = codec.decode(coded)
print(decoded)

