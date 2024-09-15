namespace WinFormsApp3
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            button1 = new Button();
            button2 = new Button();
            label3 = new Label();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Microsoft YaHei UI", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 134);
            label1.ForeColor = SystemColors.Control;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(0, 36);
            label1.TabIndex = 0;
            // 
            // button1
            // 
            button1.FlatAppearance.BorderColor = Color.White;
            button1.FlatAppearance.MouseDownBackColor = Color.FromArgb(0, 84, 168);
            button1.FlatAppearance.MouseOverBackColor = Color.FromArgb(0, 95, 189);
            button1.FlatStyle = FlatStyle.Flat;
            button1.Font = new Font("Microsoft YaHei UI", 10.5F, FontStyle.Bold, GraphicsUnit.Point, 134);
            button1.ForeColor = SystemColors.Control;
            button1.Location = new Point(603, 114);
            button1.Name = "button1";
            button1.Size = new Size(75, 29);
            button1.TabIndex = 2;
            button1.Text = "查看详情";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.FlatAppearance.BorderColor = Color.White;
            button2.FlatAppearance.MouseDownBackColor = Color.FromArgb(0, 84, 168);
            button2.FlatAppearance.MouseOverBackColor = Color.FromArgb(0, 95, 189);
            button2.FlatStyle = FlatStyle.Flat;
            button2.Font = new Font("Microsoft YaHei UI", 10.5F, FontStyle.Bold, GraphicsUnit.Point, 134);
            button2.ForeColor = SystemColors.Control;
            button2.Location = new Point(684, 114);
            button2.Name = "button2";
            button2.Size = new Size(75, 29);
            button2.TabIndex = 3;
            button2.Text = "确定";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Microsoft YaHei UI", 9.2F, FontStyle.Bold, GraphicsUnit.Point, 134);
            label3.ForeColor = SystemColors.Control;
            label3.Location = new Point(18, 57);
            label3.Name = "label3";
            label3.Size = new Size(0, 19);
            label3.TabIndex = 1;
            // 
            // Form1
            // 
            AcceptButton = button2;
            AutoScaleDimensions = new SizeF(7F, 17F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.HotTrack;
            CancelButton = button2;
            ClientSize = new Size(771, 155);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label3);
            Controls.Add(label1);
            FormBorderStyle = FormBorderStyle.None;
            KeyPreview = true;
            Name = "Form1";
            ShowInTaskbar = false;
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Button button1;
        private Button button2;
        private Label label3;
    }
}
