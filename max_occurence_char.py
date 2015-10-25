def findMaxCharCount(str_input):

    charCountArray = [0] * 256

    max = -1
    result = -1

    for e in str_input:
        charCountArray[ord(e)]+=1;

    for i in range(256):
        if max < charCountArray[i]:
            max = charCountArray[i]
            result = i

    return [max, chr(result)]

str_input = raw_input()
srt_output = findMaxCharCount(str_input)
print str(srt_output[1])+" "+str(srt_output[0])