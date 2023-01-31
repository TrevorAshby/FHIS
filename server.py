from flask import Flask, render_template, request, jsonify
import json
import base64

app=Flask(__name__, template_folder='./GUI/template', static_folder='./GUI/static') #instantiating flask object


@app.route('/')
def index():
    return render_template('gui.html')

@app.route('/saveImg', methods=['POST'])
def saveImg():
    data = request.data
    #print(data)
    json_data = json.loads(data)

    print('------')
    print(json_data['img'][23:])
    print('------')
    
    import io, base64
    from PIL import Image

    # Assuming base64_str is the string value without 'data:image/jpeg;base64,'
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(json_data['img'][23:], "utf-8"))))
    img.save('./GUI/static/imgs/my-image.jpeg')

    # with open("./GUI/static/imgs/imageToSave.jpeg", "wb") as fh:
    #     fh.write(base64.decodebytes(json_data['img'][23:]))
    #     fh.close()

    res = {
        "success":True,
    }
    print("The Res: ", res)
    return jsonify(res)

if __name__=='__main__': #calling  main 
    app.debug=True #setting the debugging option for the application instance
    app.run(host="0.0.0.0", port="3000") #launching the flask's integrated development webserver