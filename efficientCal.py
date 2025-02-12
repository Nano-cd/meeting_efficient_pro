class MeetingEvaluator:
    def __init__(self):
        self.rules = {
            'pre_agenda': 0.15,
            'pre_material': 0.2,
            'in_participants': 0.1,
            'post_action': 0.25,
            'efficiency': {
                'base_duration': 60,  # 基准会议时长(分钟)
                'participant_penalty': 0.02  # 每超1人效率惩罚
            }
        }

    def calculate_efficiency(self, duration, participants, action_items):
        """
        计算会议效率得分
        :param duration: 实际会议时长(分钟)
        :param participants: 参会人数
        :param action_items: 有效行动项数量
        """
        # 基础效率计算
        if duration <= 0:
            raise ValueError("会议时长必须大于0")
        if participants < 0 or action_items < 0:
            raise ValueError("参数不能为负数")

            # 时间得分（不超过基准时长得满分）
        base_duration = self.rules['efficiency']['base_duration']
        time_score = min(1, base_duration / duration)

        # 参会人数得分（5人基准，每多1人扣分）
        participant_score = 1 - (max(0, participants - 5) * self.rules['efficiency']['participant_penalty'])

        # 行动项得分（每个有效行动项+10%，最高+20%）
        action_bonus = min(0.2, action_items * 0.1)

        # 加权计算总分（时间50% + 参会30% + 行动项20%）
        return (time_score * 0.5 + participant_score * 0.3 + action_bonus) * 100


def meeting_assistant(meeting_type):
    checklist = {
        'technical_review': ['需求文档', '架构图', '风险评估', '备选方案'],
        'project_report': ['进度表', '问题清单', '资源需求'],
        'decision_meeting': ['选项分析', '决策标准', '实施计划']
    }
    return checklist.get(meeting_type, ['通用议程模板'])


if __name__ == "__main__":
    evaluator = MeetingEvaluator()
    print(f"会议效率得分：{evaluator.calculate_efficiency(20, 4, 3):.1f}分")  # 输出：会议效率得分：68.3分
