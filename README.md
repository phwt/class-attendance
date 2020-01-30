# class-attendance
Web Programming 2019 Assignment

## Attendance
```python
def subject(request):
    return HttpResponse('Show today subject')
```
```python
def course(request, id):
    return HttpResponse('วิชานี้สอนอะไร, มีจำนวนนักเรียนกี่คน, มีคนมาเรียน และขาดกี่คน')
```
```python
def qrcode(request):
    return HttpResponse('QR Code')

```
## Dashboard
```python
def student_list(request):
    return HttpResponse('student_list')
```
```python
def student_add(request):
    return HttpResponse('student_add')
```
```python
def student_edit(request, sid):
    return HttpResponse(f'student_edit: {sid}')
```
```python
def course_list(request):
    return HttpResponse('course_list')
```
```python
def course_add(request):
    return HttpResponse('course_add')
```
```python
def course_edit(request, cid):
    return HttpResponse(f'course_edit: {cid}')

```
## Report
```python
def dashboard(request):
    return HttpResponse('Dashboard')
```
```python
def find(request, sid):
    return HttpResponse(f'Finding: {sid}')
```