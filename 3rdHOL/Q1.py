a = "Life is too short, you need python"

if "wife" in a: print("wife") #"wife"를 'a'문장이 포함하지 않으므로 "wife"가 출력되지 않음
elif "python" in a and "you" not in a: print("python") #"python"을 'a'문장이 포함하지만 "you"도 포함하고 있어서 출력되지 않음
elif "shirt" not in a: print("shirt") #"shirt"가 'a'문장에 포함되지 않으므로 "shirt"출력됨
elif "need" in a: print("need") #위 조건문에서 true결과값이었기에 이후 elif문은 출력되지 않음
else: print("none")

#종합 결과값 : shirt