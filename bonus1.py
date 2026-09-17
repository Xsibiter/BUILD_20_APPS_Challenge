'''text = input('Enter a title: ')

length = len(text)

print("The length of the title is", length)
print(length)'''

#from pet_projects.converters1 import convert_feet_inches
#from pet_projects.parsers1 import parse

'''password = input('Enter a password: ')
while password != '11f2112':
    print('Password is not correct')
    password = input('Enter a password: ')

print('Password is correct')'''

'''x = int(input('Enter a number: '))

while x <= 10:
    x += 1
    print(x)'''

'''while True:
    name = input("What is your name? ")
    print(name.capitalize())'''

'''filenames = ["1.Raw Data.txt", "2.Report.txt", "3.Presentations.txt"]

filenames_new = []
for filename in filenames:
    filename = filename.replace(".", "-", 1)
    filenames_new.append(filename)

print(filenames_new)'''


'''waiting_list = ["Sean", "Ben","John"]
waiting_list.sort()
for index, name in enumerate(waiting_list,start=1):
    print(f"{index}.{name.capitalize()}")'''


'''contents = ["Afefef",
            "fwfowfhwfhwiofhweiofhiwefhiwfpwe",
            "wiehfweohfbipuwef;gbweiouf"]

filenames = ["efe.txt", "eqwd.txt", "dqof.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()'''


'''filenames = ["1.Raw Data.txt", "2.Report.txt", "3.Presentations.txt"]

filenames = [filename.replace(".txt", "") + 'adwswsws' for filename in filenames]

print(filenames)'''


'''date = str(input("Enter a date: "))
mood = str(input("Enter a mood: "))

thought = str(input("Enter a thought: "))

with open(f"{date}.txt", "w") as file:
    file.writelines(f"{mood}\n{thought}")'''


'''password = input("Enter a password: ")

result = {}

if len(password) < 8:
    result["length"] = False
else:
    result["length"] = True

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["uppercase"] = upper

print(result)
print(result.values())
if all(result.values()):
    print("strong password")
else:
    print("weak password")



if False in result.values():
    print("weak password")
else:
    print("strong password")'''

'''ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)'''


'''while True:
    try:
        width = float(input("Enter a width: "))
        length = float(input("Enter a length: "))
        if width == length:
            exit("It is a square")
        area = width * length
        print(area)
    except ValueError:
        print("Please enter a number")
        continue'''

'''def get_average():
    with open("data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local

average = get_average()

print(average)'''


'''feet_inches = input("Enter a feet and inches: ")

f, i = parse(feet_inches)
print(f,i)
result = convert_feet_inches(f, i)

if result < 1:
    print("The feet", feet_inches, "inches exceed the feet.")
else:
    print("Kids can slide")'''

'''import glob

myfiles = glob.glob("*.txt")
for filename in myfiles:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
print(myfiles)'''

'''import csv
with open('weather.csv', 'r') as csvfile:
    content = list(csv.reader(csvfile))
    print(content)

gibberish = input("Enter a gibberish: ")
 
for row in content:
    if row[0] == gibberish:
        print(row[2])'''

'''import shutil

shutil.make_archive("weather", "zip", "images.jpeg")'''

'''import webbrowser

user_inquiry = input("Search term ")

webbrowser.open(f"https://www.google.com/search?q={user_inquiry}")'''


'''import json

with open('questions.json', 'r') as file:
    content = file.read()
 
data = json.loads(content)


for index, question in enumerate(data):
    print(f'{index+1}) {question["question_text"]}')

    for index, alternative in enumerate(question["alternative"]):
        print(index+1,"-",alternative)
    user_answer = int(input("Answer:"))
    question["user_answer"] = user_answer

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct"
    else:
        result = "Wrong"

    message = (f"{result} for {index+1} question.\nYour answer is {question['user_answer'] } " \
               f", but the correct answer is {question['correct_answer']}")
    print(message)

print(f"Your score: {score}")'''


'''import FreeSimpleGUI as FSG
import zipfile
import pathlib

def make_archive(filepaths, dest_path):
    with zipfile.ZipFile(dest_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

label1 = FSG.Text("Select files to compress")
input1 = FSG.Input(key="files")
choose_button1 = FSG.FilesBrowse("Choose files", target="files")

label2 = FSG.Text("Select destination folder")
input2 = FSG.Input(key="folder")
choose_button2 = FSG.FolderBrowse("Choose a folder", target="folder")

compress_button = FSG.Button("Compress")
output = FSG.Text(key="output", text_color="green")

window = FSG.Window(
    "File Compressor",
    layout=[
        [label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [compress_button, output],
    ],
)

while True:
    event, values = window.read()

    if event in (FSG.WIN_CLOSED, None):
        break

    if event == "Compress":
        filepaths = [p for p in values["files"].split(";") if p]
        folder = values["folder"]

        if not filepaths or not folder:
            window["output"].update(value="Select files and a folder", text_color="red")
            continue

        dest_path = pathlib.Path(folder) / "compressed.zip"
        try:
            make_archive(filepaths, dest_path)
            window["output"].update(value="Compression completed", text_color="green")
        except OSError as exc:
            window["output"].update(value=f"Failed: {exc}", text_color="red")

window.close()'''

'''import FreeSimpleGUI as sg


def meters_from_feet_inch(feet, inches):
    meters = float(feet)*0.3048+float(inches)*0.0254
    return meters

label_feet = sg.Text("Enter feet:",)
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches:",)
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output = sg.Text(key="output", text_color="Yellow")

window = sg.Window("Feet inches -> Meters", layout=[[label_feet, input_feet],
                                                    [label_inches, input_inches],
                                                    [convert_button, output]],)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, None):
        break
    if event == "Convert":
        meters = meters_from_feet_inch(values["feet"], values["inches"])
        window["output"].update(value=f'Meters: {meters:.3f}m', text_color="cyan")
    else:
        print(f"Unknown event: {event}")

window.close()'''
