import PySimpleGUI as sg


def layout():
    # - INTERFACE PRINCIPAL DO SOFTWARE
    Title_layout = [
        [
            sg.Push(background_color='#B9D4F1'),
            sg.Text(
                'Plano Financeiro',
                font='_ 20',
                size=(45, 1),
                auto_size_text=True,
                expand_x=True,
                expand_y=True,
                justification='right',
                text_color='black',
                background_color='#B9D4F1',
            ),
            sg.Push(background_color='#B9D4F1'),
        ]
    ]

    # - TABELA FINANCEIRA
    cbox1_layout = [
        [
            sg.Button(
                k='-AdicionarBig-', button_text='Adicionar [F11]', font='_ 16'
            ),
            sg.Button(
                k='-VisualizarBig-',
                button_text='Visualizar [F10]',
                font='_ 16',
            ),
            sg.Button(k='-EditarBig-', button_text='Editar [F9]', font='_ 16'),
            sg.Button(
                k='-ExcluirBig-', button_text='Excluir [F8]', font='_ 16'
            ),
            sg.Push(background_color='#B9D4F1'),
            sg.Button(
                k='-MoverBig-',
                button_text='Mover [F7]',
                font='_ 16',
                visible=True,
            ),
        ],
        [sg.HSep()],
        [
            sg.T('Filtros', background_color='#B9D4F1'),
            sg.Button(k='-ID-', button_text='ID'),
            sg.Button(k='-Usuário Origem-', button_text='Usuário Origem'),
            sg.Button(
                k='-Dt. Origem-',
                button_text='Dt. Origem',
                button_color='DodgerBlue',
            ),
            sg.Button(k='-Modificado por-', button_text='Modificado por'),
            sg.Button(
                k='-Data de Modificação-', button_text='Data de Modificação'
            ),
            sg.Button(k='-Cod. Produto-', button_text='Cod. Produto'),
            sg.Button(k='-Serial-', button_text='Serial'),
            sg.Button(k='-Dt. Fab.-', button_text='Dt. Fab.'),
            sg.Button(k='-Lote-', button_text='Lote'),
            sg.Button(k='-Versão-', button_text='Versão'),
            sg.Button(k='-Origem-', button_text='Origem'),
            sg.Button(
                k='-Destino-', button_text='Destino', button_color='DodgerBlue'
            ),
            sg.Push(background_color='#B9D4F1'),
            sg.Button(k='-Exportar-', button_text='Exportar'),
        ],
        [
            sg.Table(
                [
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                ],
                ['um', 'dois'],
                auto_size_columns=True,
                k='-TabelaBig-',
                expand_x=False,
                expand_y=False,
                header_background_color='white',
                justification='center',
                max_col_width=60,
                background_color='#B9D4F1',
                vertical_scroll_only=False,
                enable_click_events=True,
                right_click_selects=False,
                num_rows=60,
            )
        ],
    ]

    tab_group_layout = [
        [
            sg.Tab(
                'Pesquisa',
                cbox1_layout,
                key='-TAB2-',
                background_color='#B9D4F1',
                visible=True,
            )
        ]
    ]

    layout = [
        [
            sg.Column(
                Title_layout,
                justification='center',
                background_color='#B9D4F1',
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.TabGroup(
                tab_group_layout,
                enable_events=True,
                key='-TABGROUP-',
                expand_x=True,
                expand_y=True,
                background_color='#B9D4F1',
                selected_background_color='#B9D4F1',
                tab_background_color='lightblue',
            )
        ],
    ]

    return sg.Window(
        'Plano Financeiro',
        layout,
        size=(1000, 800),
        resizable=True,
        finalize=True,
        background_color='white',
        right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
    )


window = layout()

while True:
    event, values = window.read()
