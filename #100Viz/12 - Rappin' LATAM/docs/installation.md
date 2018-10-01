# installer
```python
!conda install -c plotly plotly=3.3.0
```

### Avoid "JavaScript heap out of memory" errors during extension installation
```python
!export NODE_OPTIONS=--max-old-space-size=4096
```
### figureWidget support
```python
!jupyter labextension install plotlywidget@0.4.0 --no-build
```
### Build extensions (must be done to activate extensions since --no-build is used above)
```python
!jupyter lab build
```
### Unset NODE_OPTIONS environment variable
```python
!unset NODE_OPTIONS
```