from task_custom.default import my_task

def test_default():
    task = my_task.delay('hello')
    result = task.get()
    assert task.successful()
    assert result == 'hello'
