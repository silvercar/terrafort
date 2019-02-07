{% set counter = { 'rule_num': resource.start_count } %}
{% macro increment(dct, key, inc=1) -%}
    {% if dct.update({key: dct[key] + inc}) %} {% endif %}
{%- endmacro %}

{% for range in resource.IpRanges %}
resource "aws_security_group_rule" "{{ resource.name }}-{{ counter.rule_num }}" {
  security_group_id = "{{ resource.id }}"
  type              = "{{ resource.type }}"
  from_port         = {{ resource.FromPort | default('0')}}
  to_port           = {{ resource.ToPort | default('0')}}
  protocol          = "{{ resource.IpProtocol}}"
  cidr_blocks       = ["{{ range.CidrIp }}"]
  description       = "{{ range.Description }}"
}
{{ increment(counter, 'rule_num') }}
{% endfor %}

{% for source in resource.UserIdGroupPairs %}
resource "aws_security_group_rule" "{{ resource.name }}-{{ counter.rule_num }}" {
  security_group_id        = "{{ resource.id }}"
  type                     = "{{ resource.type }}"
  from_port                = {{resource.FromPort | default('0')}}
  to_port                  = {{resource.ToPort| default('0')}}
  protocol                 = "{{ resource.IpProtocol}}"
  source_security_group_id = "{{ source.GroupId }}"
  description              = "{{ source.Description }}"
}
{{ increment(counter, 'rule_num') }}
{% endfor %}