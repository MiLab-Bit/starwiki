## 天文馆 XR 剧情 Demo · 界面定义（精简自研版，不依赖模板 gui.rpy）

################################################################################
## 基础样式
################################################################################

style default:
    font "simhei.ttf"
    size 26
    color "#e8e6e3"
    outlines [(0, "#00000000", 0, 0)]

style button_text:
    font "simhei.ttf"

style input:
    color "#e8d9a8"
    size 28

################################################################################
## 对话框（say）—— 原版结构；仅微调字体行距与深色毛玻璃底
################################################################################

screen say(who, what):
    style_prefix "say"
    $ _bust = bust_for_who(who)

    window:
        id "window"
        xalign 0.5
        yalign 1.0
        yoffset -14
        xsize 1120
        yminimum 150
        padding (18, 16, 28, 18)
        # 原深色底板，略提高透明度，透出一点场景（毛玻璃感）
        background "#0a121dd0"
        hbox:
            spacing 16
            yalign 0.0

            if _bust:
                fixed:
                    xysize (116, 116)
                    add Solid("#152033") xysize (116, 116)
                    add _bust:
                        xysize (108, 108)
                        xoffset 4
                        yoffset 4
                    add Solid("#4a6788") xysize (116, 2) yoffset 0
                    add Solid("#4a6788") xysize (116, 2) yoffset 114
                    add Solid("#4a6788") xysize (2, 116) xoffset 0
                    add Solid("#4a6788") xysize (2, 116) xoffset 114

            vbox:
                spacing 6
                xfill True
                if who is not None:
                    text who id "who" style "say_who"
                text what id "what" style "say_dialogue"

style say_who:
    size 20
    color "#c9b896"
    outlines []
    kerning 0.5

style say_dialogue:
    size 25
    line_spacing 10
    color "#edf1f6"
    outlines []
    xmaximum 940

################################################################################
## 选项（choice / menu）
################################################################################

screen choice(items):
    style_prefix "choice"

    add "#050a1466"

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 10
        for i in items:
            textbutton i.caption action i.action

style choice_button is default:
    xsize 880
    padding (22, 14)
    background "#0c1522d0"
    hover_background "#1a3350e8"
    xalign 0.5

style choice_button_text:
    xalign 0.5
    text_align 0.5
    size 23
    color "#c5d3e4"
    hover_color "#ffffff"
    outlines []

################################################################################
## 文本输入（input）
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        xalign 0.5
        yalign 0.5
        xsize 760
        padding (40, 34)
        background "#0a121df0"
        vbox:
            spacing 20
            text prompt size 22 color "#c9b896" xalign 0.5
            input id "input" xalign 0.5

################################################################################
## 快捷菜单
################################################################################

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.985
            yalign 0.015
            spacing 14
            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("存档") action ShowMenu('save')
            textbutton _("读档") action ShowMenu('load')
            textbutton _("菜单") action MainMenu()

default quick_menu = True

style quick_button:
    background None
    padding (4, 2)

style quick_button_text:
    size 16
    color "#6f849c"
    hover_color "#dce8fa"
    outlines []

################################################################################
## 主菜单 —— 全幅 keyart + 底部文字导航（少卡片感）
################################################################################

screen main_menu():
    tag menu

    on "show" action Play("music", audio.song_theme, fadein=2.0, loop=True)

    add "images/C1_mars_keyart.png":
        fit "cover"
        xysize (1280, 720)
    add Solid("#040910aa")
    # bottom gradient plate
    add Solid("#040910e6"):
        xsize 1280
        ysize 220
        yalign 1.0

    vbox:
        xpos 56
        ypos 420
        spacing 6
        text _("天文馆 XR") size 44 color "#ffffff" outlines []
        text _("沉浸式剧情样片") size 18 color "#9aaebb" outlines []
        null height 4
        text _("上海端点星幻境科技有限公司") size 15 color "#7f93a8" outlines []
        text _("制作 · 吟游诗人Lab") size 14 color "#657889" outlines []

    vbox:
        xpos 56
        ypos 600
        spacing 8
        textbutton _("开始体验") action Start() style "nav_text_btn"
        textbutton _("读取进度") action ShowMenu("load") style "nav_text_btn"
        textbutton _("退出") action Quit(confirm=True) style "nav_text_btn"

    text _("主题曲 · The Road Home / 星河有归") size 13 color "#5d7186" xalign 0.98 yalign 0.97 outlines []

style nav_text_btn is default:
    background None
    padding (0, 4)
    xalign 0.0

style nav_text_btn_text:
    size 24
    color "#c5d3e4"
    hover_color "#ffffff"
    outlines []

style menu_big_button is default:
    xsize 420
    padding (20, 12)
    background "#0c1522d8"
    hover_background "#1a3350e8"
    xalign 0.5

style menu_big_button_text:
    xalign 0.5
    size 22
    color "#c5d3e4"
    hover_color "#ffffff"
    outlines []

################################################################################
## 剧情线选择 —— 双栏海报，而非堆按钮
################################################################################

screen story_select():
    tag menu
    modal True

    add "images/P_space.png":
        fit "cover"
        xysize (1280, 720)
    add "#040910b8"

    text _("选择体验线") size 18 color "#8fa3b8" xpos 56 ypos 36 outlines []
    text _("「[player_name]」") size 28 color "#ffffff" xpos 56 ypos 62 outlines []

    hbox:
        xalign 0.5
        yalign 0.48
        spacing 28

        button:
            action Return("mars")
            xysize (460, 420)
            padding (0, 0)
            background "#00000000"
            hover_background "#ffffff10"
            fixed:
                add "images/C1_mars_keyart.png":
                    fit "cover"
                    xysize (460, 420)
                add Solid("#04101899"):
                    yalign 1.0
                    xysize (460, 120)
                vbox:
                    yalign 1.0
                    xalign 0.0
                    xpos 22
                    ypos -22
                    spacing 4
                    text _("航向火星") size 28 color "#ffffff" outlines []
                    text _("好莱坞生存剧 · 约 15–20 分钟") size 15 color "#a8bccf" outlines []

        button:
            action Return("princeton")
            xysize (460, 420)
            padding (0, 0)
            background "#00000000"
            hover_background "#ffffff10"
            fixed:
                add "images/P_keyart.png":
                    fit "cover"
                    xysize (460, 420)
                add Solid("#04101899"):
                    yalign 1.0
                    xysize (460, 120)
                vbox:
                    yalign 1.0
                    xalign 0.0
                    xpos 22
                    ypos -22
                    spacing 4
                    text _("回到普林斯顿") size 28 color "#ffffff" outlines []
                    text _("魔法圈叙事 · 约 15–20 分钟") size 15 color "#a8bccf" outlines []

    hbox:
        xalign 0.5
        yalign 0.93
        spacing 36
        textbutton _("主题曲 · 星河有归") action Return("theme") style "nav_text_btn"

################################################################################
## 主题曲片尾 · 出品+歌词同一条滚轴（前奏定格出品，再整体上滚）
################################################################################

## 前奏定格后上滚；缩短时长以加快节奏（曲长 ~382s）
define THEME_ROLL_SEC = 200.0
## 滚轴终点
define THEME_ROLL_END_Y = -5200

transform theme_credits_roll(intro=28.0, duration=200.0, end_y=-5200):
    yanchor 0.0
    ypos 96
    pause intro
    linear duration ypos end_y

screen theme_lyrics():
    tag menu
    modal True

    on "show" action Play("music", audio.song_theme, fadein=1.5, loop=True)

    add "images/P_dome_star.png":
        fit "cover"
        xysize (1280, 720)
    add "#02060eb8"

    fixed:
        at theme_credits_roll(THEME_INTRO_SEC, THEME_ROLL_SEC, THEME_ROLL_END_Y)
        xsize 1280

        vbox:
            xalign 0.5
            xmaximum 760
            spacing 8

            null height 40

            ## —— 出品 / 制作（与歌词同轴，前奏期间停在画面中）——
            text _("出品") size 15 color "#c41e3a" xalign 0.5
            null height 6
            text _("上海端点星幻境科技有限公司") size 30 color "#f3f0e8" xalign 0.5 text_align 0.5
            null height 28
            text _("制作人") size 15 color "#c41e3a" xalign 0.5
            null height 6
            text _("AIGC艺术家 · 吟游诗人Lab") size 24 color "#e8e0d4" xalign 0.5
            null height 28
            text _("歌名") size 15 color "#c41e3a" xalign 0.5
            null height 6
            text _("The Road Home") size 26 color "#f3f0e8" xalign 0.5
            text _("星河有归") size 20 color "#a09888" xalign 0.5

            null height 56
            add Solid("#8a909666") xsize 80 ysize 1 xalign 0.5
            null height 56

            ## —— 歌词（接在名单后，随同一条轴上滚）——
            text _("Beneath the silence of the universe") size 22 color "#f3f0e8" xalign 0.5
            text _("Where ancient starlights sleep") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("在宇宙寂静的深处") size 17 color "#9a9080" xalign 0.5
            text _("古老的星光沉沉安眠") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("A lonely signal drifts beyond") size 22 color "#f3f0e8" xalign 0.5
            text _("The oceans of the deep") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("一道孤独的讯号漂向远方") size 17 color "#9a9080" xalign 0.5
            text _("穿越深邃无垠的海洋") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("Through endless tides of time and space") size 22 color "#f3f0e8" xalign 0.5
            text _("Through shadows of the night") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("穿越时间与空间的无尽潮汐") size 17 color "#9a9080" xalign 0.5
            text _("穿过漫漫长夜的幽影") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("A thousand fading stars remember") size 22 color "#f3f0e8" xalign 0.5
            text _("A distant hidden light") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("千万颗正在消逝的星辰") size 17 color "#9a9080" xalign 0.5
            text _("仍记得那遥远而隐秘的光") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("If fate is but a broken compass") size 22 color "#f3f0e8" xalign 0.5
            text _("Lost beneath the sky") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("若命运不过是一枚破碎的罗盘") size 17 color "#9a9080" xalign 0.5
            text _("遗落在苍穹之下") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("Let the winds of endless ages") size 22 color "#f3f0e8" xalign 0.5
            text _("Carry echoes home tonight") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("便让无尽岁月的风") size 17 color "#9a9080" xalign 0.5
            text _("带着古老的回响，于今夜归来") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("At the edge of the universe") size 24 color "#f3f0e8" xalign 0.5
            text _("Where the last stars fall") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("在宇宙的边缘") size 17 color "#b0a898" xalign 0.5
            text _("最后的星辰正在坠落") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("A thousand worlds, a thousand dreams") size 24 color "#f3f0e8" xalign 0.5
            text _("Still answer to the call") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("千万世界，千万梦想") size 17 color "#b0a898" xalign 0.5
            text _("仍回应着那古老的召唤") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("Through silver skies and oceans blue") size 24 color "#f3f0e8" xalign 0.5
            text _("Through every road unknown") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("穿越银色的天空 · 穿越蔚蓝的海洋") size 17 color "#b0a898" xalign 0.5
            text _("穿过所有未知的道路") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("All paths beneath the heavens") size 24 color "#f3f0e8" xalign 0.5
            text _("Will lead the lost back home") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("苍穹之下所有的道路") size 17 color "#b0a898" xalign 0.5
            text _("终将引领迷途之灵回归故乡") size 17 color "#b0a898" xalign 0.5

            null height 36
            text _("Eternity is not the endless time") size 22 color "#f3f0e8" xalign 0.5
            text _("Nor words forever carved in stone") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("永恒并非无尽流逝的时间") size 17 color "#9a9080" xalign 0.5
            text _("也不是刻在石上的不朽誓言") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("It is the silent light beyond the stars") size 22 color "#f3f0e8" xalign 0.5
            text _("That calls all wandering souls back home") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("它是群星之外那束寂静的光") size 17 color "#9a9080" xalign 0.5
            text _("呼唤所有漂泊的灵魂回归") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("There were seas without a shoreline") size 22 color "#f3f0e8" xalign 0.5
            text _("There were kingdoms made of dust") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("曾有无岸之海") size 17 color "#9a9080" xalign 0.5
            text _("曾有尘埃筑成的王国") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("There were names beneath the ages") size 22 color "#f3f0e8" xalign 0.5
            text _("Lost to time and rust") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("曾有名字埋藏于漫长岁月") size 17 color "#9a9080" xalign 0.5
            text _("被时间与锈蚀遗忘") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("The heavens kept their ancient songs") size 22 color "#f3f0e8" xalign 0.5
            text _("The galaxies their flame") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("苍穹保存着古老的歌谣") size 17 color "#9a9080" xalign 0.5
            text _("银河守护着不灭的火焰") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("Until the last wandering comet") size 22 color "#f3f0e8" xalign 0.5
            text _("Returned unto its name") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("直到最后一颗流浪的彗星") size 17 color "#9a9080" xalign 0.5
            text _("回归它曾属于的名字") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("Perhaps the stars were written") size 22 color "#f3f0e8" xalign 0.5
            text _("Before the dawn of time") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("也许星辰早已被写下") size 17 color "#9a9080" xalign 0.5
            text _("在黎明与时间诞生之前") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("Perhaps each broken fragment") size 22 color "#f3f0e8" xalign 0.5
            text _("Was searching to align") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("也许每一片破碎的碎片") size 17 color "#9a9080" xalign 0.5
            text _("都在寻找彼此的契合") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("When the final moon is sleeping") size 22 color "#f3f0e8" xalign 0.5
            text _("When the ancient worlds are gone") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("当最后的月亮沉睡") size 17 color "#9a9080" xalign 0.5
            text _("当远古的世界消亡") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("I will follow every signal") size 22 color "#f3f0e8" xalign 0.5
            text _("Until the last light carries on") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("我仍会追随每一道讯号") size 17 color "#9a9080" xalign 0.5
            text _("直到最后的光芒继续燃烧") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("Beyond the veil of endless skies") size 22 color "#f3f0e8" xalign 0.5
            text _("Beyond the fading years") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("越过无尽天空的帷幕") size 17 color "#9a9080" xalign 0.5
            text _("越过逐渐消逝的岁月") size 17 color "#9a9080" xalign 0.5

            null height 22
            text _("The stars will sing the forgotten song") size 22 color "#f3f0e8" xalign 0.5
            text _("That once brought us back here") size 22 color "#f3f0e8" xalign 0.5
            null height 4
            text _("群星将再次唱起那被遗忘的歌") size 17 color "#9a9080" xalign 0.5
            text _("那首曾带我们回到此处的歌") size 17 color "#9a9080" xalign 0.5

            null height 36
            text _("At the edge of the universe") size 24 color "#f3f0e8" xalign 0.5
            text _("Where all horizons fade") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("在宇宙的尽头") size 17 color "#b0a898" xalign 0.5
            text _("当所有地平线渐渐消融") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("The stars remember ancient vows") size 24 color "#f3f0e8" xalign 0.5
            text _("The paths the cosmos made") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("群星仍记得古老的誓言") size 17 color "#b0a898" xalign 0.5
            text _("记得宇宙曾留下的道路") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("Through every world that ever was") size 24 color "#f3f0e8" xalign 0.5
            text _("Through every dream once known") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("穿越曾存在过的每个世界") size 17 color "#b0a898" xalign 0.5
            text _("穿越每一个曾被知晓的梦境") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("All rivers flowing through the heavens") size 24 color "#f3f0e8" xalign 0.5
            text _("Will find their way back home") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("流经天穹的万千河流") size 17 color "#b0a898" xalign 0.5
            text _("终将寻回自己的归途") size 17 color "#b0a898" xalign 0.5

            null height 36
            text _("Not a place") size 24 color "#f3f0e8" xalign 0.5
            text _("Not a time") size 24 color "#f3f0e8" xalign 0.5
            null height 4
            text _("不是一个地方") size 17 color "#b0a898" xalign 0.5
            text _("不是一个时代") size 17 color "#b0a898" xalign 0.5

            null height 22
            text _("Only the light") size 26 color "#f3f0e8" xalign 0.5
            text _("That knows the way home") size 26 color "#f3f0e8" xalign 0.5
            null height 4
            text _("唯有那束光") size 19 color "#b0a898" xalign 0.5
            text _("仍知归途") size 19 color "#b0a898" xalign 0.5

            null height 80
            text _("感谢聆听") size 15 color "#7a7268" xalign 0.5
            null height 720

    text _("点击或 Esc 返回") size 13 color "#6a6258" xalign 0.98 yalign 0.98

    key "K_ESCAPE" action Return()
    key "K_RETURN" action Return()
    key "mouseup_1" action Return()
    key "dismiss" action Return()

################################################################################
## 体验结束选择
################################################################################

screen end_select():
    tag menu
    modal True

    add "#040910cc"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 14
        text _("体验结束") size 22 color "#8fa3b8" xalign 0.5 outlines []
        null height 8
        textbutton _("返回剧情选择") action Return("hub") style "nav_text_btn" xalign 0.5
        textbutton _("听主题曲 · 星河有归") action Return("theme") style "nav_text_btn" xalign 0.5
        textbutton _("结束体验") action Return("quit") style "nav_text_btn" xalign 0.5

################################################################################
## 存档 / 读档
################################################################################

screen file_slots(title):
    tag menu

    add "#0a0f1a"

    vbox:
        xalign 0.5
        yalign 0.08
        text title size 40 color "#ffffff" xalign 0.5

    grid 3 2:
        xalign 0.5
        yalign 0.5
        spacing 24

        for i in range(1, 7):
            button:
                action FileAction(i)
                xsize 340
                ysize 190
                background "#14213ac8"
                hover_background "#2c4f8ae0"
                vbox:
                    spacing 8
                    add FileScreenshot(i) xysize (300, 118)
                    text FileTime(i, format=_("%Y-%m-%d %H:%M"), empty=_("空档位")):
                        size 18 color "#9fc0e8" xalign 0.5

    textbutton _("返回"):
        xalign 0.5
        yalign 0.95
        action Return()
        style "menu_big_button"

screen save():
    use file_slots(_("保存进度"))

screen load():
    use file_slots(_("读取进度"))

################################################################################
## 确认对话框
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add "#00000099"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        padding (50, 44)
        background "#0b1220f0"
        vbox:
            spacing 34
            text _(message) size 26 xalign 0.5 text_align 0.5
            hbox:
                xalign 0.5
                spacing 90
                textbutton _("确定") action yes_action style "menu_big_button" xsize 200
                textbutton _("取消") action no_action style "menu_big_button" xsize 200

################################################################################
## 通知 / 跳过指示
################################################################################

screen notify(message):
    zorder 100

    frame:
        xalign 0.02
        yalign 0.03
        padding (24, 12)
        background "#14213ad0"
        text "[message!tq]" size 22 color "#ffd77a"

    timer 3.25 action Hide('notify')

screen skip_indicator():
    zorder 100
    text _("▸▸ 快进中…") size 22 color "#ffd77a" xalign 0.02 yalign 0.1

################################################################################
## Diegetic HUD —— 头盔/控制台式生命体征面板（嵌入世界，非浮窗菜单）
## 由 mars_rescue.rpy 的状态变量驱动；仅在火星线显示
################################################################################

screen hud():
    zorder 50
    if hud_visible:
        frame:
            xpos 20
            ypos 18
            background "#071018d0"
            padding (14, 10)
            xsize 268
            vbox:
                spacing 5
                text _("启明基地") size 13 color "#7f93a8" outlines []
                hbox:
                    spacing 10
                    text _("O2  [o2_pct]%") size 16 color ("#9fe6a0" if o2_pct > 40 else "#ff8f8f") outlines []
                    text _("PWR  [power_pct]%") size 16 color ("#e6c88a" if power_pct > 25 else "#ff8f8f") outlines []
                text _("[mars_clock]") size 14 color "#c5d3e4" outlines []
                text _("[mars_objective]") size 13 color "#8fa3b8" xmaximum 240 outlines []
                if hud_alarm:
                    text _("系统警报") size 13 color "#ff8f8f" outlines []

screen comms_ticker():
    zorder 50
    if hud_visible and comms_last:
        text "[comms_last]" size 12 color "#7dcea0" xpos 20 ypos 148 xmaximum 268 outlines []

screen watch():
    zorder 50
    if watch_visible:
        frame:
            xalign 0.985
            ypos 18
            background "#120e08d0"
            padding (14, 10)
            vbox:
                spacing 5
                text _("怀表") size 13 color "#a89068" outlines []
                hbox:
                    spacing 16
                    vbox:
                        text _("你") size 12 color "#8fa3b8" outlines []
                        text "[watch_you]" size 16 color "#ffffff" outlines []
                    vbox:
                        text _("地球") size 12 color "#8fa3b8" outlines []
                        text "[watch_earth]" size 16 color ("#e6c88a" if watch_gamma > 1.01 else "#ffffff") outlines []
                text "gamma = [watch_gamma]" size 12 color ("#ff8f8f" if watch_gamma > 2.0 else "#9fe6a0") outlines []
