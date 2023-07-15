# [2D RPG](https://www.youtube.com/playlist?list=PLEkX-p0oUs8zdcKGN8SZrRfumnTV0lAsk)

## 目次

- [2D RPG](#2d-rpg)
  - [目次](#目次)
  - [サブタイトル1](#サブタイトル1)
  - [サブタイトル2](#サブタイトル2)
    - [サブタイトル2-1](#サブタイトル2-1)
      - [サブタイトル2-1-1](#サブタイトル2-1-1)

## サブタイトル1

ここに本文1を書く

## サブタイトル2

ここに本文2を書く

### サブタイトル2-1

ここに本文2-1を書く

#### サブタイトル2-1-1

ここに本文2-1-1を書く

- リストアイテム1
- リストアイテム2
- リストアイテム3

**強調テキスト**

*斜体テキスト*

[リンクテキスト](http://リンク先URL.com)

![画像altテキスト](http://画像URL.com)

> 引用テキスト

`コードスニペット`

---

<details>
<summary>折りたたむタイトル</summary>

ここには折りたたむ部分の内容を書きます。

</details>


1. 画面サイズを「960 x 540」程度にする
2. https://pipoya.net/sozai/ images/Character配下にキャラクター画像を移動する
3. Map配下に画像を移動(640 x 480)
4. sprite modeを「Multiple」pixels per unitを「32」filter modeを「point(no filter)」formatを「RGBA 32 bit」にしてApply
5. Sprite Editorで分割
6. PlayerController.tsを作成
<details>
    <summary>PlayerController.ts</summary>

```shell

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class PlayerController : MonoBehaviour
{
  // Update is called once per frame
  void Update()
  {
    float x = Input.GetAxisRaw("Horizontal");
    float y = Input.GetAxisRaw("Vertical");

    transform.position += new Vector3(x, y, 0);
  }
}

```
* 移動が速すぎる
   </details>
7. ひとマス移動