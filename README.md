# FLET リアクティブ・コントロール

参考 : [Python(Flet)でリアクティブなUIを作る方法を考える](https://qiita.com/ForestMountain1234/items/64edacd5275c1ce4c943)

## [パッケージ構造](https://www.codogue.com/asciitree)
```
main.py
flet_reactive_controls  
├ state.py  
│ ├ State  
│ └ ReactiveStat  
├ text.py  
│ └ ReactiveText
└ example.py
　 └ main
```

## state.py
class State : 状態管理クラス

reactive_control_obj = State(T)

