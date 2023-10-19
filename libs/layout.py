    # - INTERFACE PRINCIPAL DO SOFTWARE
    Title_layout = [
        [
            sg.Image(data=ico),
            sg.Push(background_color='#B9D4F1'),
            sg.Text(
                sw_name + 'v' + version,
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
            sg.Text(
                'DESENVOLVIDO PELA GERÊNCIA DE FABRICAÇÃO E TESTE(GFT)',
                font='_ 7',
                size=(66, 1),
                justification='right',
                text_color='black',
                background_color='#B9D4F1',
            ),
        ]
    ]

    # - CONTAGEM DE PRODUTOS NÃO CONFORME
    cbox3_layout = [
        [
            sg.T('Destino:', background_color='#B9D4F1'),
            sg.Combo(
                sorted(json_object['listdestino']) + ['Todos'],
                default_value='Todos',
                background_color='#B9D4F1',
                k='-ConterFilter-',
                enable_events=True,
            ),
            sg.Push(background_color='#B9D4F1'),
            sg.Button(k='-ExportarResumo-', button_text='Exportar'),
        ],
        [sg.HSep()],
        [
            sg.Table(
                tableresume,
                columsresumo,
                auto_size_columns=True,
                k='-TabelaResumo-',
                expand_x=True,
                expand_y=True,
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
    # - INTERFACE INICIAL (CADASTRO DE NÃO CONFORMIDADES)
    cbox0_layout = [
        [
            sg.Button(k='-Adicionar-', button_text='Adicionar', font='_ 16'),
            sg.Button(k='-Visualizar-', button_text='Visualizar', font='_ 16'),
            sg.Button(k='-Editar-', button_text='Editar', font='_ 16'),
            sg.Button(k='-Excluir-', button_text='Excluir', font='_ 16'),
        ],
        [sg.HSep()],
        [
            sg.Table(
                table,
                colums,
                auto_size_columns=True,
                k='-TabelaPrincipal-',
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
    # - PESQUISA NO HISTÓRICO DE PRODUTOS NÃO CONFORMES
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
                visible=True if PERMISSION[2] == '1' else False,
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
                tablebig,
                columsbig,
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

    # - CONFIGURAÇÕES DE CADASTRO DE PRODUTOS NÃO CONFORMES
    cbox2_layout = [
        [
            sg.T(
                'Cadastro de Produtos',
                font='_ 20',
                size=(35, 1),
                background_color='#B9D4F1',
            )
        ],
        [
            sg.Combo(
                sorted(combo_list),
                size=(20, 10),
                enable_events=True,
                k='-Combo-',
            )
        ],
        [
            sg.Button(
                button_text='Modificar', k='-Selecionar-', s=15, font='_ 16'
            ),
            sg.Button(
                button_text='Adicionar Novo',
                k='-Adicionar Novo-',
                s=18,
                font='_ 16',
            ),
            sg.Button(
                button_text='Excluir',
                k='-Excluir Cadastro-',
                s=15,
                font='_ 16',
            ),
            sg.Button(
                button_text='Configurações Gerais',
                k='-Configurações Gerais-',
                s=20,
                font='_ 16',
            ),
        ],
    ]
    tab_group_layout = [
        [
            sg.Tab(
                'Principal',
                cbox0_layout,
                visible=True,
                key='-TAB1-',
                background_color='#B9D4F1',
            ),
            sg.Tab(
                'Pesquisa',
                cbox1_layout,
                key='-TAB2-',
                background_color='#B9D4F1',
                visible=True,
            ),
            sg.Tab(
                'Resumo',
                cbox3_layout,
                key='-TAB3-',
                background_color='#B9D4F1',
                visible=True,
            ),
            sg.Tab(
                'Configurações',
                cbox2_layout,
                key='-TAB4-',
                background_color='#B9D4F1',
                visible=True if PERMISSION[2] == '1' else False,
            ),
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

    window = sg.Window(
        sw_name + 'v' + version,
        layout,
        icon='icone.ico',
        size=size_monitor((20000, 2000), 0.9),
        resizable=True,
        finalize=True,
        background_color='white',
        right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
    )