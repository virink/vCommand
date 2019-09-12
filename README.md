# vCommand

A command tools for me

## Functions

- [*]     macstr      - MAC地址转换
- [x]    str2ascii    - 字符串 -> ASCII
- [x]     str2ord     - 字符串 -> ASCII
- [x]    ascii2str    - ASCII -> 字符串 (逗号分隔)
- [x]     ord2str     - ASCII -> 字符串
- [x]     dec2hex     - Dec -> Hex
- [x]     hex2dec     - Hex -> Dec
- [x]    byte2hex     - Byte -> Hex
- [x]    str2byte     - 字符串 -> Byte
- [x]     str2hex     - 字符串 -> Hex
- [x]    hex2byte     - Hex -> Byte
- [x]     hex2str     - 字符串 -> Hex
- [x]     ip2hex      - IP -> Hex
- [x]     hex2ip      - Hex -> IP
- [x]     dec2ip      - Dec -> IP
- [x]     ip2dec      - IP -> Dec
- [x]      b64d       - Base64 Decode
- [x]      b64e       - Base64 Encode
- [x]      b32d       - Base32 Decode
- [x]      b32e       - Base32 Encode
- [x]      b16d       - Base16 Decode
- [x]      b16e       - Base14 Encode
- [x]     atbash      - 埃特巴什码解码
- [x]     caesar      - 凯撒编码
- [x]      rot13      - rot13
- [x]      mpkc       - 手机键盘编码 Mobile Phone Keyboard Cipher
- [x]      morse      - 摩斯电码
- [x]     peigen      - 培根密码
- [x]    vigenere     - 维吉利亚密码
- [x]      urld       - URL 解码
- [x]    urldecode    - URL 解码
- [x]      urle       - URL 编码
- [x]    urlencode    - URL 编码
- [x]      urldp      - URL 解码 Plus
- [x] urldecode_plus  - URL 解码 Plus
- [x]      urlep      - URL 编码 Plus
- [x] urlencode_plus  - URL 编码 Plus
- [x]      ctfr       - CFTR 查询子域名 Search By https://crt.sh
- [x]       png       - PNG 文件格式分析
- [x]     githack     - GitHack Git源码泄露下载

## Install

~~pip install vcommand~~
`pip install vcommand-0.1.1-py3.7.egg`

```shell
# 用于 zsh & zsh-syntax-highlighting
echo 'eval $($(which vcommand) _alias)' >> ~/.zshrc
# bash
echo 'eval $($(which vcommand) _alias)' >> ~/.bashrc
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