from collections import defaultdict
import re
from math import sqrt

class Codec:
    def __init__(self) -> None:
        self.protocol_pattern = r'((?:https?://)|(?:ftp://)|(?:mailto://)|(?:file//)|(?:data//))(.*)'
        self.encoder = {}
        self.decoder = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url = re.match(self.protocol_pattern, longUrl)
        protocol = url.group(1)
        path = url.group(2)

        if path in self.encoder:
            return protocol + self.encoder[path]
        else:
            key = str(len(self.encoder.keys()))
            self.encoder[path] = key
            self.decoder[key] = path
            return protocol + self.encoder[path]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url = re.match(self.protocol_pattern, shortUrl)
        protocol = url.group(1)
        key = url.group(2)

        return protocol + self.decoder[key]
        
if __name__ == '__main__':
    # 1 <= url.length <= 10 ** 4 -> possiblity of url <= (26 + 26 + 10 + 9) * 10 ** 4
    url = "http://leetcode.com/problems/design-tinyurl/"
    codec = Codec()
    print(codec.decode(codec.encode(url)))
