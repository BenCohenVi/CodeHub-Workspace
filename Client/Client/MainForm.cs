﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Client
{
    public partial class MainForm : Form
    {
        public ClientSocket cSock;
        private string lastSelected;
        private Bunifu.Framework.UI.Drag dr = new Bunifu.Framework.UI.Drag();
        public MainForm(ClientSocket clientSock, string username)
        {
            InitializeComponent();
            this.cSock = clientSock;
            projectTab1.SetSocket(this.cSock);
            nameLabel.Text = username;
        }

        private void exitBtn_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }

        private void minBtn_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void projectsTab_Click(object sender, EventArgs e)
        {
            seperatorLine.Width = projectsTabB.Width;
            seperatorLine.Left = projectsTabB.Left;
            projectTab1.Visible = false;
            projectTab1.BringToFront();
            bunifuTransition1.ShowSync(projectTab1);
        }

        private void commentsTab_Click(object sender, EventArgs e)
        {
            seperatorLine.Width = commentsTabB.Width;
            seperatorLine.Left = commentsTabB.Left;
            this.lastSelected = projectTab1.Get_Latest();
            commentsTab1.SetTab(this.cSock, this.lastSelected);
            commentsTab1.Visible = false;
            commentsTab1.BringToFront();
            bunifuTransition1.ShowSync(commentsTab1);
        }

        private void shareTab_Click(object sender, EventArgs e)
        {
            seperatorLine.Width = shareTabB.Width;
            seperatorLine.Left = shareTabB.Left;
            this.lastSelected = projectTab1.Get_Latest();
            sharedTab1.SetTab(this.cSock, this.lastSelected);
            sharedTab1.Visible = false;
            sharedTab1.BringToFront();
            bunifuTransition1.ShowSync(sharedTab1);
        }

        private void bunifuImageButton1_Click(object sender, EventArgs e)
        {
            panel3.Visible = true;
        }

        private void bunifuFlatButton3_Click(object sender, EventArgs e)
        {
            Application.Restart();
        }

        private void cancelBtn_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }

        private void panel4_MouseDown(object sender, MouseEventArgs e)
        {
            this.dr.Grab(this);
        }

        private void panel4_MouseMove(object sender, MouseEventArgs e)
        {
            this.dr.MoveObject();
        }

        private void panel4_MouseUp(object sender, MouseEventArgs e)
        {
            this.dr.Release(); 
        }

        private void bunifuFlatButton1_Click(object sender, EventArgs e)
        {
            placeLabel.Text = "My Profile";
            projectsTabB.Visible = true;
            commentsTabB.Visible = true;
            shareTabB.Visible = true;
            projectsTabB.Enabled = true;
            commentsTabB.Enabled = true;
            shareTabB.Enabled = true;
            seperatorLine.Visible = true;
        }

        private void bunifuFlatButton2_Click(object sender, EventArgs e)
        {
            placeLabel.Text = "Search User";
            projectsTabB.Visible = false;
            commentsTabB.Visible = false;
            shareTabB.Visible = false;
            projectsTabB.Enabled = false;
            commentsTabB.Enabled = false;
            shareTabB.Enabled = false;
            seperatorLine.Visible = false;
        }
    }
}