﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Client
{
    public partial class UserTab : UserControl
    {
        ClientSocket cSock;
        private string projects;
        private string username;
        public UserTab()
        {
            InitializeComponent();
            foreach (Control Item in this.Controls)
        }

        public void Set_Tab(ClientSocket cliSock, string projects, string username)
        {
            projectList.Items.Clear();
            versionList.Items.Clear();
            this.username = username;
            this.cSock = cliSock;
            this.projects = projects;
            this.projects = this.Fix_Format(this.projects);
        }

        public string Fix_Format(string project)

        public void Set_Table()

        private void projectList_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
        }
    }
}