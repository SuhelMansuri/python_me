major = ('Physics', 'Chemistry', 'Mathematics', 'Music', 'Comp.sc')
more_subjects = ('History',)
print(type(more_subjects))
print(type(major))

major = major + more_subjects

print('new_major : ',major)

lst_major = list(major)
print(lst_major)
lst_major.append('History')
print(lst_major)
major = tuple(lst_major)
print(major)