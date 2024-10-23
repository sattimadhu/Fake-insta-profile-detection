from flask import Flask,render_template,request
from model.main import predict_profile
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/main', methods=['GET', 'POST'])
def main():
    info = [None] * 8  # Pre-allocate a list of 8 elements.
    if request.method == 'POST':
        # Collect form data and ensure numeric fields are converted properly
        try:
            info[0] = float(request.form.get('follower', 0)) or 0
            info[1] = float(request.form.get('following', 0)) or 0 
            info[2] = float(request.form.get('bio', 0)) or 0
            info[3] = float(request.form.get('media', 0)) or 0
            info[4] = 1 if request.form.get('profile')=='yes' or request.form.get('profile')=='1' else 0 
            info[5] = 1 if request.form.get('isprivate')=='yes' or request.form.get('isprivate')=='1' else 0
            info[6] = int(request.form.get('usernamedig', 0)) or 0
            info[7] = int(request.form.get('usernamelen', 0)) or 0

            result = predict_profile(info)
            return render_template('index.html', result=result)

        except ValueError as e:
            # Handle conversion errors gracefully
            return render_template('index.html', error=f"Invalid input: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)