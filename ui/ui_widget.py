import urwid


class ContactTreeWidget(urwid.TreeWidget):
    """ Display widget for leaf nodes """

    def selectable(self):
        return True

    def get_display_text(self):
        children_text = self.get_node().get_value()['name']
        return urwid.SelectableIcon(children_text)


class NTreeNode(urwid.TreeNode):
    """ Data storage object for leaf nodes """

    def load_widget(self):
        return ContactTreeWidget(self)


class NParentNode(urwid.ParentNode):
    """ Data storage object for interior/parent nodes """

    def load_widget(self):
        return ContactTreeWidget(self)

    def load_child_keys(self):
        data = self.get_value()
        return range(len(data['children']))

    def load_child_node(self, key):
        """Return either an NTreeNode or ExampleParentNode"""
        childdata = self.get_value()['children'][key]
        childdepth = self.get_depth() + 1
        if 'children' in childdata:
            childclass = NParentNode
        else:
            childclass = NTreeNode
        return childclass(childdata, parent=self, key=key, depth=childdepth)
