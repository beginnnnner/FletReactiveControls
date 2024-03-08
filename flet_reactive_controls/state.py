from typing import TypeVar, Generic, Union, Callable

T = TypeVar('T')

#状態管理クラス。bind()で状態変更時に呼び出したい処理を登録できる。
class State(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._observers: list[Callable] = []

    def get(self):
        return self._value #値の参照はここから

    def set(self, new_value: T):
        if self._value != new_value:
            self._value = new_value #新しい値をセット
            for observer in self._observers: observer() #変更時に各observerに通知する

    def bind(self, observer):
        self._observers.append(observer)# 変更時に呼び出す為のリストに登録

# ...Stateクラスの定義...

# 依存しているStateの変更に応じて値が変わるクラス。
class ReactiveState(Generic[T]):
    #formula: State等を用いて最終的にT型の値を返す関数。
    #例えばlambda: f'value:{state_text.get()}'といった関数を渡す。

    #reliance_states: 依存関係にあるStateをlist形式で羅列する。
    def __init__(self, formula: Callable[[], T], reliance_states: list[State]):
        self.__value = State(formula())# 通常のStateクラスとは違い、valueがStateである
        self.__formula = formula
        self._observers: list[Callable] = []

        for state in reliance_states:
            #依存関係にあるStateが変更されたら、再計算処理を実行するようにする
            state.bind(lambda : self.update())

    def get(self):
        return self.__value.get()

    def update(self):
        old_value = self.__value.get()
        #コンストラクタで渡された計算用の関数を再度呼び出し、値を更新する
        self.__value.set(self.__formula())

        if old_value != self.__value.get():
            for observer in self._observers: observer() #変更時に各observerに通知する

    def bind(self, observer):
        self._observers.append(observer)# 変更時に呼び出す為のリストに登録


# ...StateクラスとReactiveStaetクラスの定義...

# リアクティブなコンポーネントの引数(ReactiveStateを追加)
StateProperty = Union[T, State[T], ReactiveState[T]]

# コンポーネント内でpropsに、Stateになる可能性のある引数を渡す。
# StateやReactiveStateが渡された場合、自動でbind_funcを変更検知イベントに登録する
def bind_props(props: list[StateProperty], bind_func: Callable[[], None]):
    for prop in props:
        if isinstance(prop, State) or isinstance(prop, ReactiveState):
            prop.bind(lambda : bind_func())

# Stateであれば.get()メソッドを呼び出し、通常の変数であればそのまま値を取得する
def get_prop_value(prop: StateProperty):
    if isinstance(prop, State):
        return prop.get()
    elif isinstance(prop, ReactiveState):
        return prop.get()
    else:
        return prop