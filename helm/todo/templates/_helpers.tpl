{{- define "todo-chart.name" -}}
{{- default .Chart.Name .Values.nameOverride -}}
{{- end -}}

{{- define "todo-chart.fullname" -}}
{{- printf "%s-%s" (include "todo-chart.name" .) .Release.Name -}}
{{- end -}}
