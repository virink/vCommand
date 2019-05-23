# vCommand

A command tools for me

## Functions

-      b16e       - Base14 Encode
-      b16d       - Base16 Decode
-      b32e       - Base32 Encode
-      b32d       - Base32 Decode
-      b64e       - Base64 Encode
-      b64d       - Base64 Decode
-     atbash      - 埃特巴什码解码
-     caesar      - 凯撒编码
-      rot13      - rot13
-      mpkc       - 手机键盘编码 Mobile Phone Keyboard Cipher
-      morse      - 摩斯电码
-     peigen      - 培根密码
-    vigenere     - 维吉利亚密码
-      urld       - URL 解码
-    urldecode    - URL 解码
-      urle       - URL 编码
-    urlencode    - URL 编码
-      urldp      - URL 解码 Plus
- urldecode_plus  - URL 解码 Plus
-      urlep      - URL 编码 Plus
- urlencode_plus  - URL 编码 Plus
-    str2ascii    - 字符串 -> ASCII
-     str2ord     - 字符串 -> ASCII
-    ascii2str    - ASCII -> 字符串 (逗号分隔)
-     ord2str     - ASCII -> 字符串
-     dec2hex     - Dec -> Hex
-     hex2dec     - Hex -> Dec
-    byte2hex     - Byte -> Hex
-    str2byte     - 字符串 -> Byte
-     str2hex     - 字符串 -> Hex
-    hex2byte     - Hex -> Byte
-     hex2str     - 字符串 -> Hex
-     ip2hex      - IP -> Hex
-     hex2ip      - Hex -> IP
-     dec2ip      - Dec -> IP
-     ip2dec      - IP -> Dec

## Install

~~pip install vcommand~~

```bash
# 用于 zsh-syntax-highlighting
echo 'eval $($(which vcommand) _alias)' >> ~/.zshrc
```

**快捷命令???**
```bash
function command_not_found_handler(){
    if {which vcommand > /dev/null} {
        $(which vcommand) $@
    } else {
        echo "[!] zsh: command not found: $0"
    }
}
```

## Usage

```bash
vcommand func
```