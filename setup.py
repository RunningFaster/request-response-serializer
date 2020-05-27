from setuptools import setup, find_packages

setup(
    name='request_response_json_serializer',
    version='0.0.1',
    description='Python框架Django，Flask序列化request和response',
    long_description=open('README.rst').read(),
    license='License',
    install_requires=[
        'Django>=2.0',
        'Flask>=1.0',
        'djangorestframework>=3.0'
    ],
    packages=['request_response_json_serializer'],  # 要打包的项目文件夹
    include_package_data=True,  # 自动打包文件夹内所有数据
    author='RunningFaster',
    author_email='ren754203791@126.com',
    url='https://github.com/RunningFaster/request-response-serializer.git',
    # packages = find_packages(include=("*"),),
)
