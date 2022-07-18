from django import forms

class TicketForm(forms.Form):
        title = forms.CharField(label='タイトル', required=True, max_length=50)
        description =forms.CharField(widget=forms.Textarea,label='備考欄', max_length=255)
        task_status = forms.ChoiceField(label='ステータス', required=True)
        limit_time = forms.TimeField(label='期限')
        create_at = forms.DateTimeField(label='作成日時')
        update_at = forms.DateTimeField(label='更新日時')
