def conv(name,word):
    from pdf2docx import Converter,parse

    cv = Converter(name)
    cv.convert(str(word).split("@")[0]+".docx",0,None)
    cv.close()
    return str(word).split("@")[0]+".docx"

