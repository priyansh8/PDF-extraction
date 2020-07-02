def Get_text_from_image():
    import pytesseract,io,gc
    from PIL import Image
    from wand.image import Image as wi
    import gc
    """ Extracting text content from Image  """

    pdf=wi(filename='C:\\Users\\user\\Desktop\\Labs\\INE033L07EO0.pdf',resolution=300)                                                                                                                
    pdfImg=pdf.convert('jpeg')                                                                                                                                                                              
    imgBlobs=[]
    extracted_text=[]
    try:        
        for img in pdfImg.sequence:
            page=wi(image=img)
            imgBlobs.append(page.make_blob('jpeg'))
            for i in range(0,5):
                [gc.collect() for i in range(0,10)]

        for imgBlob in imgBlobs:
            im=Image.open(io.BytesIO(imgBlob))
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'
            text=pytesseract.image_to_string(im,lang='eng')
            text = text.replace(r"\n", " ")
            extracted_text.append(text)
            for i in range(0,5):
                [gc.collect() for i in range(0,10)]
        return (''.join([i.replace("\n"," ").replace("\n\n"," ") for i in extracted_text]))
        [gc.collect() for i in range(0,10)]
    finally:
        [gc.collect() for i in range(0,10)]
        img.destroy()

print(Get_text_from_image())
