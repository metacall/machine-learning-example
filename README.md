# MetaCall Machine Learning Example
A repository to host Machine Learning examples for Metacall.

The file `run_model.py` has actual exported function, and it is exposed in the `metacall.json` file.

## The `predict_salary` function
It expects a 2d array of integers as **input**, output is predicted salaries.

```sh
curl -X POST https://api.metacall.io/<your_alias>/python-machine-learning-example/v1/call/predict_salary --data '{"input":[[3],[6]]}'
```

<a href='https://ko-fi.com/B0B4MFVE' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=1' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
