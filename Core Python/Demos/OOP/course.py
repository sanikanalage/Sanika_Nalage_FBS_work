class Course:
    def __init__(self,courseID,courseName,duration,fees):
        self.courseID=courseID
        self.courseName=courseName
        self.duration=duration
        self.fees=fees

    def getCourseId(self):
        return self.courseID
    def setCourseId(self,newCourseID):
        self.courseID=newCourseID

    def getCourseName(self):
        return self.courseName
    def setCourseName(self,newCourseName):
        self.courseName=newCourseName

    def getDuration(self):
        return self.duration
    def setDuration(self,newDuration):
        self.duration=newDuration

    def getFees(self):
        return self.fees
    def setFees(self,newFees):
        self.fees=newFees


    def disply(self):
        print(f'CourseID={self.courseID},CourseName={self.courseName},Duration={self.duration},Fees={self.fees}')

c1=Course(11029,"Python Data Science","6 Months","35700")
c2=Course(11022,'Data Analytics','4 Months','27000')
print(c1.getCourseId())
print(c1.getCourseName())
print(c2.getDuration())
print(c2.getFees())
c2.setDuration('5 Months')
c2.disply()