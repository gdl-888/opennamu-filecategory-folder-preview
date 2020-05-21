            if name == '분류:파일':
                div += '''
                    <style>
                        .xp-icon-link {
                            display: inline-block;
                            vertical-align: top;
                        }

                        .xp-icon {
                            display: inline-block;
                            margin: 5px;
                        }

                        .xp-icon td {
                            border: none;
                            background: transparent;
                        }

                        .xp-icon-container {
                            width: 96px;
                            height: 96px;
                            background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAABD0lEQVR4nO3SPUoDURiG0dn/EiyzArfgBlKkt7Oz0C5l0kQU8wOCc3PJc154qmFg+M4si5nZlDsMyi7ssH3ZDGmBcLZhx4dwvuHHh/C9ux3/F8KjNy9AoVsIxb9xSH8C+Hpp/7nTP/UT4iaAw4+BuApw7w8sBABAOwAA2gEA0A4AgHYAALQDAKAdAADtAABoBwBAOwAA2gEA0A4AgHYAZgb4eHvWygEA0A4AgHYAALQDAKAdAADtAABoBwBAOwAA2gEA0A4AgHYAALQDAKAdAADtAMwM8P76pJUDAKAdAADtAABoBwBAOwAA2gEA0A4AgHYAALQDAKAdAADtAABoBwBAOwATAyynh1o/M7MZdgREziYFLq9OHgAAAABJRU5ErkJggg==) !important;
                        }

                        .xp-icon-container img {
                            width: 44px;
                            height: 38px;
                        }

                        .xp-icon-label {
                            text-align: center;
                        }
                    </style>
                '''
            cdiv = ''
            if re.search('^분류[:]파일[/]', name):
                cdiv += '''
                    <style>
                        .xp-icon {
                            display: inline-block;
                            margin: 5px;
                        }

                        .xp-icon-container {
                            width: 96px;
                            height: 96px;
                            background-size: cover !important;
                        }

                        .xp-icon-label {
                            text-align: center;
                        }
                    </style>

                    <script>
                        $(function() {
                            $(".xp-icon-container").click(function() {
                                var thisObj = $(this);
                                $("#imgPreviewFrame").attr("src", thisObj.attr("data-image-src"));
                            });
                        });
                    </script>

                    <div style="overflow: scroll; white-space: nowrap;">
                '''

            u_div = ''
            ucnt = 0
            ccnt = 0

            for data in back:
                if re.search('^분류:', data[0]):
                    if name == '분류:파일':
                        curs.execute("select link from back where title = ? and type = 'cat'", [data[0]])
                        imglst = curs.fetchall()

                        try:
                            piece = os.path.splitext(imglst[0][0].replace(imglst[0][0].split(':')[0] + ':', ''))
                            i1s = sha224(piece[0]) + piece[1]
                        except:
                            i1s = ''
                        try:
                            piece = os.path.splitext(imglst[1][0].replace(imglst[1][0].split(':')[0] + ':', ''))
                            i2s = sha224(piece[0]) + piece[1]
                        except:
                            i2s = ''
                        try:
                            piece = os.path.splitext(imglst[2][0].replace(imglst[2][0].split(':')[0] + ':', ''))
                            i3s = sha224(piece[0]) + piece[1]
                        except:
                            i3s = ''
                        try:
                            piece = os.path.splitext(imglst[3][0].replace(imglst[3][0].split(':')[0] + ':', ''))
                            i4s = sha224(piece[0]) + piece[1]
                        except:
                            i4s = ''

                        u_div += '''
                            <a href="/w/''' + url_pas(data[0]) + '''" class=xp-icon-link>
                                <table class=xp-icon>
                                    <tbody>
                                        <tr>
                                            <td class=xp-icon-container>
                                                <table style="margin: 0 auto auto 3px;">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width: 44px; height: 33px; background: url('/image/''' + i1s + '''\') center top; background-size: cover;"></td>
                                                            <td style="width: 44px; height: 33px; background: url('/image/''' + i2s + '''\') center top; background-size: cover;"></td>
                                                        </tr>

                                                        <tr>
                                                            <td style="width: 44px; height: 33px; background: url('/image/''' + i3s + '''\') center top; background-size: cover;"></td>
                                                            <td style="width: 44px; height: 33px; background: url('/image/''' + i4s + '''\') center top; background-size: cover;"></td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>

                                        <tr>
                                            <td class=xp-icon-label>
                                                ''' + html.escape(data[0]) + '''
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </a>
                        '''
                    else:
                        u_div += '<li><a href="/w/' + url_pas(data[0]) + '">' + data[0] + '</a></li>'

                    ucnt += 1
                else:
                    if re.search("^분류[:]파일[/]", name):
                        piece = os.path.splitext(data[0].replace(data[0].split(':')[0] + ':', ''))
                        imgsrc = sha224(piece[0]) + piece[1]

                        cdiv += '''
                            <a class=xp-icon>
                                <table>
                                    <tbody>
                                        <tr>
                                            <td class=xp-icon-container data-image-src="/image/''' + imgsrc + '''" style="background: url(\'/image/''' + imgsrc + '''\') center top;">
                                            </td>
                                        </tr>

                                        <tr>
                                            <td class=xp-icon-label>
                                                <a href="/w/''' + url_pas(data[0]) + '''">
                                                    ''' + html.escape(data[0]) + '''
                                                </a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </a>
                        '''
                    else:
                        cdiv += '<li><a href="/w/' + url_pas(data[0]) + '">' + data[0] + '</a></li>'

                    ccnt += 1

            if re.search('^분류[:]파일[/]', name):
                cdiv += '</div><img id=imgPreviewFrame></img>'
