import main
def test_example_function():
    code=main.main(runtype='test')
    if code==0:
        print('test passed')
    else:
        #引发错误
        raise Exception('test failed')