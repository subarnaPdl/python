class personal:
    mobileNum = 9800000000


class business:
    workNum = 9811111111

# Here details is a sub class and personal & business are main classes.
class details(personal, business):
    name = "Subarna Poudel"
    age = 18

    def prin(self):
        self.mobileNum = 9812345678
        print(f"Changed mobile number is {self.mobileNum}.")
        print(f"Unchanged work number is {self.workNum}.")

st = details()
print(st.mobileNum)
print(st.workNum)
st.prin()
