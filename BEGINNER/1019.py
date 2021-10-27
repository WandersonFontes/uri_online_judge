# Time Conversion

seconds = int(input())
hours = int(seconds/60/60)
minutes = int((seconds / 60) - (hours * 60))
seconds = int(seconds - ((hours*60*60) + (minutes * 60)))
print(str(hours)+':'+str(minutes)+':'+str(seconds))