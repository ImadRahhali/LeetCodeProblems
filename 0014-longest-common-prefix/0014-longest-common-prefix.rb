# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    prefix = ""
    length = strs.map { |s| s.length }.min
    0.upto(length - 1) do |i|
        char = strs[0][i]
        strs.each { |s| return prefix if s[i] != char }
        prefix += char
    end
    prefix
end